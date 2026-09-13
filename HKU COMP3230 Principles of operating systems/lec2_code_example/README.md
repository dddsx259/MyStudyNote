## Build

```bash
make
```

## Run

```bash
taskset -c 0 ./cpu "I am A" 5                         # CPU virtualization
taskset -c 0 ./cpu "I am A" 5 & taskset -c 0 ./cpu "I am B" 5 & taskset -c 0 ./cpu "I am C" 5 & wait # three processes share CPU 0

setarch x86_64 -R ./mem 100 5                        # forbit ASLR (Address Space Layout Randomization)
setarch x86_64 -R ./mem 100 5 & setarch x86_64 -R ./mem 200 5 & setarch x86_64 -R ./mem 300 5 & wait 

./threads 100000             # intentional race
./threads_mutex 100000       # mutex-protected version

./io                         # writes io_demo_output.txt
cat io_demo_output.txt
```

`cpu` and `mem` run for five rounds by default, with a one-second busy wait per
round. The race program is intentionally unsafe; its final value is not
guaranteed. `threads_mutex` should always produce `2 * loops`.

Use `make clean` to remove compiled executables.
