# labels
### `<html>`
+ Defines the root of an HTML document.
+ All other elements must be descendants of this element.
+ Common attributes:
  + `lang`:
    + Specifies the language of the document.
    + Example: `<html lang="en">` for English.
  + `dir`:
    + Specifies the text direction for the document.
    + Values: `ltr` (left-to-right), `rtl` (right-to-left), `auto` (determines direction based on content).
    + Example: `<html dir="ltr">` for left-to-right text.
+ Example:
```html
<!DOCTYPE html>
<html lang="en">
</html>
```

### `<head>`
+ Contains metadata and resources for the document.
+ Common children:
  + `<meta>`: defines metadata such as charset or viewport.
  + `<title>`: sets the document title shown in browser tabs.
  + `<link>`: references external resources like stylesheets.
  + `<script>`: includes or references JavaScript.
+ Example:
```html
<head>
  <meta charset="UTF-8">
  <title>Document Title</title>
</head>
```

### `<body>`
+ Contains the visible content of the document.
+ Common children:
  + `<header>`
  + `<nav>`
  + `<main>`
  + `<section>`
  + `<article>`
  + `<footer>`
  + `<div>`
+ Example:
```html
<body>
  <header>...</header>
</body>
```

### `<header>`
+ Defines introductory or navigational content.
+ Often contains logos, headings, or navigation.
+ Example:
```html
<header>
  <h1>Site Title</h1>
</header>
```

### `<nav>`
+ Defines a section with navigation links.
+ Example:
```html
<nav>
  <a href="#home">Home</a>
  <a href="#about">About</a>
</nav>
```

### `<main>`
+ Represents the main content of the document.
+ There should be only one `<main>` per page.
+ Example:
```html
<main>
  <article>...</article>
</main>
```

### `<section>`
+ Defines a thematic grouping of content.
+ Can contain headings, paragraphs, lists, and other sections.
+ Example:
```html
<section>
  <h2>Section Title</h2>
  <p>Section content.</p>
</section>
```

### `<article>`
+ Represents self-contained content that can stand alone.
+ Example:
```html
<article>
  <h2>Article Title</h2>
  <p>Article text.</p>
</article>
```

### `<footer>`
+ Defines footer content for a section or page.
+ Example:
```html
<footer>
  <p>Copyright © 2026</p>
</footer>
```

### `<div>`
+ Generic block-level container.
+ Used to group elements for styling or scripting.
+ Example:
```html
<div class="container">
  <p>Block content.</p>
</div>
```

### `<span>`
+ Generic inline container.
+ Used for styling or grouping text within other elements.
+ Example:
```html
<p>This is <span class="highlight">important</span> text.</p>
```

### `<h1>` to `<h6>`
+ Heading elements with decreasing importance.
+ `<h1>` is the top-level heading, `<h6>` is the least important.
+ Example:
```html
<h1>Main Title</h1>
<h2>Subheading</h2>
```

### `<p>`
+ Defines a paragraph of text.
+ Example:
```html
<p>This is a paragraph.</p>
```

### `<a>`
+ Defines a hyperlink.
+ Common attributes:
  + `href`: URL of the link.
  + `target`: where to open the linked document (`_blank`, `_self`).
+ Example:
```html
<a href="https://example.com" target="_blank">Visit Example</a>
```

### `<img>`
+ Embeds an image.
+ Common attributes:
  + `src`: image source URL.
  + `alt`: alternative text for accessibility.
  + `width`, `height`: size of the image.
+ Example:
```html
<img src="image.jpg" alt="Description" width="300">
```

### `<ul>`
+ Defines an unordered list.
+ Contains `<li>` items.
+ Example:
```html
<ul>
  <li>Item one</li>
  <li>Item two</li>
</ul>
```

### `<ol>`
+ Defines an ordered list.
+ Contains `<li>` items.
+ Example:
```html
<ol>
  <li>First item</li>
  <li>Second item</li>
</ol>
```

### `<li>`
+ Defines a list item.
+ Used inside `<ul>`, `<ol>`, or `<menu>`.
+ Example:
```html
<li>List item</li>
```

### `<table>`
+ Defines a table for tabular data.
+ Common children:
  + `<caption>`: table caption.
  + `<thead>`:
    + `<tr>`:
      + `<th>`
  + `<tbody>`:
    + `<tr>`:
      + `<td>`
  + `<tfoot>`:
    + `<tr>`:
      + `<td>`
+ Example:
```html
<table>
  <caption>Sample Table</caption>
  <thead>
    <tr>
      <th>Header 1</th>
      <th>Header 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Cell 1</td>
      <td>Cell 2</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="2">Footer</td>
    </tr>
  </tfoot>
</table>
```

### `<form>`
+ Defines an interactive form for user input.
+ Common children:
  + `<label>`
  + `<input>`
  + `<textarea>`
  + `<select>`:
    + `<option>`
  + `<button>`
   Defines a clickable button.
   Common types: `button`, `submit`, `reset`.
   Example:
  + `<fieldset>`:
    + `<legend>`
+ Example:
```html
<form action="/submit" method="post">
  <label for="name">Name:</label>
  <input id="name" name="name" type="text">
  <button type="submit">Submit</button>
</form>
```

### `<label>`
+ Defines a label for a form control.
+ `for` attribute links to an input's `id`.
+ Example:
```html
<label for="email">Email:</label>
<input id="email" type="email">
```

### `<input>`
+ Defines an input control.
+ Common types: `text`, `email`, `password`, `checkbox`, `radio`, `submit`.
+ Example:
```html
<input type="text" name="username">
```

### `<textarea>`
+ Defines a multi-line text input.
+ Example:
```html
<textarea name="message" rows="4"></textarea>
```

### `<select>`
+ Defines a dropdown list.
+ Contains `<option>` elements.
+ Example:
```html
<select name="choices">
  <option value="1">Option 1</option>
  <option value="2">Option 2</option>
</select>
```

### `<button>`
+ Defines a clickable button.
+ Common types: `button`, `submit`, `reset`.
+ Example:
```html
<button type="submit">Send</button>
```



