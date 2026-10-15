/*
* Name: Dai Yuxuan
* UID: 3036292116
* Platform: dev on WSL2
* Remark: ALl complete.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>
#include <signal.h>

char **tokenize(char *sent){
    //Split the string into words
    int n=0;
    char **toks = malloc(30 * sizeof(char *));
    char *p = sent;
    while(*p != '\0'){
        while(*p != '\0' && isspace((unsigned char)*p))p++;
        if(*p == '\0')break;
        char *start = p;
        while(*p != '\0' && !isspace((unsigned char)*p))p++;
        size_t len = (size_t)(p-start);
        char *tok = malloc(len+1);
        memcpy(tok, start, len);
        tok[len] = '\0';
        toks[n++] = tok;
    }
    toks[n] = NULL;
    return toks;
}

char *read_line(void){
    //Read the input line of user
    printf("## 3230yash >>    ");
    char *line = NULL;
    size_t cap = 0;
    ssize_t len = getline(&line, &cap, stdin);
    if (len == -1){
        free(line);
        return NULL;
    }
    if (len > 0 && line[len-1] == '\n')
        line[len-1] = '\0';
    return line;
}

int check_pipe(char *line){
    //Check if the pipe is correct(the usage of '|')
    char **toks = tokenize(line);
    if(toks == NULL || toks[0] == NULL)return 0;
    int n = 0;
    while(toks[n] != NULL)n++;
    if(strcmp(toks[0], "|") == 0 || strcmp(toks[n - 1], "|") == 0){
        printf("3230yash: Incorrect pipe sequence\n");
        return 1;
    }
    for(int i=0; i<n; i++){
        if(strcmp(toks[i], "||") == 0){
            printf("3230yash: should not have two consecutive | without in-between command\n");
            return 1;
        }
        if(i < n-1 && strcmp(toks[i], "|") == 0 && strcmp(toks[i+1], "|") == 0){
            printf("3230yash: should not have two consecutive | without in-between command\n");
            return 1;
        }
    }
    return 0;
}

void exec_fail(const char *cmd){
    //Print exec error then exit child
    if(errno == EACCES)
        fprintf(stderr, "3230yash: '%s': Permission denied\n", cmd);
    else
        fprintf(stderr, "3230yash: '%s': No such file or directory\n", cmd);
    fflush(stderr);
    _exit(127);
}

void report_signaled(const char *cmd, int status){
    //Report if a child was killed by a signal
    if(!WIFSIGNALED(status)) return;
    const char *sname = strsignal(WTERMSIG(status));
    if(sname == NULL) sname = "Unknown";
    printf("%s:  %s\n", cmd, sname);
}

int read_stat_line(pid_t pid, char *out, size_t outsz){
    //Read one /proc/pid/stat snapshot into out
    char path[64];
    char buf[4096];
    snprintf(path, sizeof(path), "/proc/%d/stat", (int)pid);
    FILE *f = fopen(path, "r");
    if(f == NULL) return -1;
    if(fgets(buf, sizeof(buf), f) == NULL){ fclose(f); return -1; }
    fclose(f);

    char *rp = strrchr(buf, ')');
    if(rp == NULL) return -1;
    rp++;
    while(*rp == ' ') rp++;

    char state = 0;
    unsigned long minflt = 0, majflt = 0, utime = 0, stime = 0, vsize = 0;
    int processor = 0;
    char *save = NULL;
    char *tok = strtok_r(rp, " ", &save);
    int idx = 0;
    while(tok != NULL){
        if(idx == 0) state = tok[0];
        else if(idx == 7) minflt = strtoul(tok, NULL, 10);
        else if(idx == 9) majflt = strtoul(tok, NULL, 10);
        else if(idx == 11) utime = strtoul(tok, NULL, 10);
        else if(idx == 12) stime = strtoul(tok, NULL, 10);
        else if(idx == 20) vsize = strtoul(tok, NULL, 10);
        else if(idx == 36){ processor = (int)strtol(tok, NULL, 10); break; }
        idx++;
        tok = strtok_r(NULL, " ", &save);
    }
    if(idx < 36) return -1;

    long clk = sysconf(_SC_CLK_TCK);
    if(clk <= 0) clk = 100;
    snprintf(out, outsz, "%c %d %.2f %.2f %lu %lu %lu",
             state, processor,
             (double)utime / (double)clk,
             (double)stime / (double)clk,
             vsize, minflt, majflt);
    return 0;
}

void watch(char **argv){
    //inbuilt function for watch

    if(argv == NULL || argv[0] == NULL) return;

    int syncp[2];
    if(pipe(syncp) < 0) return;

    pid_t pid = fork();
    if(pid < 0){
        close(syncp[0]); close(syncp[1]);
        return;
    }

    if(pid == 0){
        close(syncp[1]);
        char c;
        if(read(syncp[0], &c, 1) < 0){}
        close(syncp[0]);
        signal(SIGINT, SIG_DFL);
        execvp(argv[0], argv);
        exec_fail(argv[0]);
    }

    close(syncp[0]);
    char snaps[256][128];
    int nsnap = 0;
    if(read_stat_line(pid, snaps[nsnap], sizeof(snaps[0])) == 0)
        nsnap++;
    write(syncp[1], "x", 1);
    close(syncp[1]);

    while(1){
        usleep(500000);
        siginfo_t info;
        memset(&info, 0, sizeof(info));
        int wr = waitid(P_PID, pid, &info, WEXITED | WNOHANG);
        if(wr == 0 && info.si_pid == pid){
            if(nsnap < 256 && read_stat_line(pid, snaps[nsnap], sizeof(snaps[0])) == 0)
                nsnap++;
            break;
        }
        if(nsnap < 256 && read_stat_line(pid, snaps[nsnap], sizeof(snaps[0])) == 0)
            nsnap++;
    }

    printf("STATE CPUID UTIME STIME VSIZE     MINFLT MAJFLT\n");
    for(int i=0; i<nsnap; i++)
        printf("%s\n", snaps[i]);
}

char *execute(char *line){
    //execute the command
    if(line == NULL){
        printf("Invalid input. Please try again.\n");
        return NULL;
    }
    char *p = line;
    char ***argvs = malloc(20 * sizeof(char **));
    int fd[20][2];
    int n=0;
    while(*p != '\0'){
        while(*p != '\0' && isspace((unsigned char)*p))p++;
        if(*p == '\0')break;

        char *start = p;
        while(*p != '\0' && *p != '|')p++;
        size_t len = (size_t)(p-start);
        if (*p == '|') p++;

        char *sent = malloc(len+1);
        memcpy(sent, start, len);
        sent[len] = '\0';

        argvs[n++] = tokenize(sent);
        free(sent);
    }
    if(n == 0)
        return NULL;

    for(int i=0; i<n; i++){
        if(argvs[i] == NULL || argvs[i][0] == NULL){
            if(i == 0 || i == n-1)
                printf("3230yash: Incorrect pipe sequence\n");
            else
                printf("3230yash: should not have two consecutive | without in-between command\n");
            return NULL;
        }
    }

    if(strcmp(argvs[0][0], "watch") == 0){
        if(n > 1){
            printf("3230yash: Cannot watch a pipe sequence\n");
            return NULL;
        }
        watch(&argvs[0][1]);
        return NULL;
    }
    else if(n == 1 && strcmp(argvs[0][0], "exit") == 0){
        if(argvs[0][1] != NULL){
            printf("3230yash: \"exit\" with other arguments!!!\n");
            return NULL;
        }
        printf("3230yash: Terminated\n");
        return "EXIT";
    }

    pid_t pids[20];
    for(int i=0; i<n-1; i++)
        pipe(fd[i]);

    for(int i=0; i<n; i++){
        pids[i] = fork();
        if(pids[i]==0){
            if(i>0)
                dup2(fd[i-1][0], STDIN_FILENO);
            if(i<n-1)
                dup2(fd[i][1], STDOUT_FILENO);

            for (int j = 0; j < n - 1; j++) {
                close(fd[j][0]);
                close(fd[j][1]);
            }
            signal(SIGINT, SIG_DFL);
            execvp(argvs[i][0], argvs[i]);
            exec_fail(argvs[i][0]);
        }
    }
    for (int i = 0; i < n - 1; i++) {
        close(fd[i][0]);
        close(fd[i][1]);
    }
    for (int i = 0; i < n; i++){
        int status = 0;
        waitpid(pids[i], &status, 0);
        report_signaled(argvs[i][0], status);
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    char *line;
    while(1){
        line = read_line();
        if(check_pipe(line)==1)continue;
        if(execute(line) == "EXIT")break;
        free(line);
    }
    return 0;
}
