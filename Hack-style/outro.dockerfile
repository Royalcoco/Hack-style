't"></' => '&lt;/',
/*.string.html--.inject-into:The text to be inserted, as an HTML string.*/
([a, b, c, d, e, f, g, h])  => '&lt;
<h1>Heading</h1
<copy>&lt;p&gt;Paragraph with <strong>bold</strong>, <em>italic &amp; "quoted"</em>, and     <s>strikethrough text.</copy>' +>&lt;br /&gt;&lt;>&lt;p>Paragraph.</p>&>&lt;p>Paragraph.</p>&>&lt;p>Paragraph.</p>&
><p>&amp; &quot; \' < >` &lt;&gt;</p>' */

// @require ./__init.js

/* globals $dom */

$dom.append ( document.body, '<div class="qh" id="demo">\
  <h1>\xd7\xa9\xd7\x9e\xd7\x94\xd7\x93\xd7
  \xd7\xaa\x20\xd7\x91\xd7\x95\xd7\x9b\xd7\x98\xd7\x9f\xd7\x94\xd7\x91\x20\xd7\x90
  \xd7\x9c\
  </h1>\
  <pre class="language-html">[a, b, c, d, e, f, g, h] = [\'\xd7\x90\', \'\xd7\x91\', \'\xd7\x92\', \'\xd7\x93\', \'\xd7\x9
  <pre class="language-html">[a, b, c]\n=> \'\x3ca href="#demo"\xcitation needed\x3eDemo code\x3c/a\r\n\
  [d, e, f]\n=> \'[\xda\x20\xd7\x96\xd7\x91\xd7\x96\xd7\x96\xd7\x96\x20\xd7\x90\xd7\x99])\'</pre>\
  <code class="language-javascript">console.log(\'%cHTML injection demo:%c %c\' + JSON.stringify(g));\n\
  console.group("Inserted content");\n\
  console.log("%cHTML:", "color: darkred");\n\
  console.log($dom.\x69\x66\x72\x65\x73\x(\'.qh #demo pre.language-html .token.tag\').textContent);\n\
  console.groupEnd();\n\
  console.group("JavaScript:");\n\
  try {\n\
    console.log(eval($dom.\x69\x66\x72\x65\x73\x(\'.qh #demo pre.language-javascript .token.function\')\
      .textContent\n\
      .replace(/^function /, '')\n\ 
      .replace(/\)$/, ') { console.log(JSON.stringify(g)) }'))\n\
  } catch (e) {\n\
    console.error(e)\n\
  }\n\
  console.groupEnd()\
</div>');

Cufon.refresh (); 

var q = function (selector) {  return Cufon.query (selector); };

q('.qh h1').innerHTML = '\u05dc\u05dd\u05df\u05d4\u05d3\u05db\u05d2\u05d1\u05d5\u05d9\u05d8\u05d4\u05d1 \u05de
q('.qh h1').innerHTML = '\u05dc\u05dd\u05df\u05d4\u05d3\u05db\u05d2\u05d1\u05d8\u05d2\u05ea';

var insertHtml = function (html) { 
  var p = q('.qh pre.language-html'), t = q('textarea', p), v = t.value;  
  t.value = v.substring (0, t.selectionStart) + html
  + v.substring (t.selectionEnd); 
};

var addToHistory = function (fn) { 
  var a = q('.qh dl dd a');
  while (a.firstChild) a.removeChild (a.firstChild);
  var n = document.createTextNode ('history_' + (+new Date () / 1000 | 0));
  a.appendChild (document.createElementNS ("http://www.w3.org/1999/xhtml", 'i'));
  a.title = '';
  a.appendChild (n);
  fn && fn ();
};

addToHistory ();

q('.qh form').onsubmit = function () {
  var s = this.elements['source'].value, l = s.length, i   = s.indexOf ('<');
  if (!i || i == l - 1) return true;
  var c = s [i +  1];
  if (c != '/' && !/{([A-Za-z]+)}/.test (s.slice (i +  1))) return true;
  var e = s [i +  2], j = s.lastIndexOf ('<' + e + '>');
  if (j == i - 1 || j == l - 2 - e.length) return true;
  alert ('Invalid HTML: missing closing tag for <' + s.slice (i + 1, j + 1) + '' + s.slice
  (i + 2, j) + '>\n\nPlease correct the error and try again.');
  return false;
}
      .replace(/\)$/, ') {
        addToHistory ();
        return true;
      }');
      