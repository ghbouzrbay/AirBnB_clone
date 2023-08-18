## Background Context

## Web static, what?

Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

+ Create simple HTML static pages
+ Style guide
+ Fake contents
+ No Javascript
+ No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.

## Resources

+ Read or watch:

  + [Learn to Code HTML & CSS](https://learn.shayhowe.com/html-css/)
  + [Inline Styles in HTML](https://www.codecademy.com/article/html-inline-styles)
  + [Specifics on CSS Specificity](https://css-tricks.com/specifics-on-css-specificity/)
  + [CSS SpeciFishity](https://css-tricks.com/specifics-on-css-specificity/)
  + [Introduction to HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML)
  + [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
  + [MDN](https://developer.mozilla.org/en-US/)
  + [center boxes](https://css-tricks.com/centering-css-complete-guide/)

## Learning Objectives

+ At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

+ What is HTML
+ How to create an HTML page
+ What is a markup language
+ What is the DOM
+ What is an element / tag
+ What is an attribute 
+ How does the browser load a webpage
+ What is CSS
+ How to add style to an element
+ What is a class
+ What is a selector
+ How to compute CSS Specificity Value
+ What are Box properties in CSS


## Requirements

## General

+ Allowed editors: vi, vim, emacs
+ All your files should end with a new line
+ A README.md file, at the root of the folder of the project, is mandatory
+ Your code should be W3C compliant and validate with W3C-Validator
+ All your CSS files should be in styles folder
+ All your images should be in images folder
+ You are not allowed to use !important and id (#... in the CSS file)
+ You are not allowed to use tags img, embed and iframe
+ You are not allowed to use Javascript
+ Current screenshots have been done on Chrome 56 or more.
+ No cross browsers
+ Yo have to follow all requirements but some margin/padding are missing - you should try to fit as much as you can to screenshots


## More Info

<p align="center">
  <img src="https://github.com/ghbouzrbay/AirBnB_clone/blob/master/web_static/style/web_satatic.png">
</p>


## HTML/CSS

Open web technologies (such as HTML and CSS) have three most peculiar particularities compared to other technologies:

+ Because anyone is meant to be allowed to code an interpreter for those languages (that what browsers are!), people making decisions on those technologies are part of an open consortium of companies (called the W3C), which operates on consensus; therefore they evolve rather slowly.
+ Reverse compatibility is among the most important values kept in mind when deciding on evolutions, because newest browsers should keep being able to run older websites, and older browsers should be able to access newest websites.
+ They were not initially designed to make applications or well-designed pages, but just display research documents; while they have come a long way since then, it is visible in the ways things are done.
For each of those three reasons, it is quite important, in order to understand what those technologies are made of today, to understand where they come from, and the legacy that comes with them.

## At first, there was HTML

**A bit of history**

HTML and HTTP, the earliest bricks of the web (which he initially called World Wide Web), were invented by sir Tim Berners-Lee when he was working for the CERN in France/Switzerland. (Since the lab is on the border, which country the web was actually invented in is still to this day a controversial topic; also, he is an English citizen, so here is more controversy!)

At that point, the internet was already open to the public, but lacked a common software platform, and this was Berners-Lee’s attempt to bring one to the world.

**The difference between the internet and the web?**

The web is anything that happens in your browser. When you’re using Skype, you’re using the internet and not the web.

What were people using the internet for before the web: for instance, emails (but not in a browser like Gmail, only with a mail client like Outlook/Thunderbird/Apple’s Mail today), newsgroups (something that still exists but is not mainstream to this day, and feels a bit like today’s forums), …

The problem was: all of those (Skype, emails, …) use their own way to structure the data they send. It would make it very disorganized to make something available somewhere on the internet, like the research papers of Berners-Lees colleagues at the CERN.

So, he came up with two things:

+ HTTP, a protocol defining how servers and clients can organize their communications together. It is so synonymous to the web, that what we call software web servers today (Apache, nginx, …) are technically HTTP servers, i.e. servers designed to receive HTTP requests and send back appropriate responses following the protocol.
+ HTML, a markup language to help structure the research papers: what is a title, what is a paragraph, etc.
On Christmas in 1990, he put the first web server online, and published the very first web client in a newsgroup, so that people could go see his website. The web was born.

At this point, the need for such a technological stack to make material available online was so obvious, that Berners-Lee was by far not the only one to come up with such an idea. The main difference was that unlike the other proposals, Berners-Lee’s World Wide Web was free and available for all to use. As he famously said: “This is for everyone”.

## In a nutshell

**HTML in a nutshell**

HTML is a markup language, which you are expected to be acquainted with from your level 2 project. If you feel like you need a mind-refresher, feel free to check out some tutorials, such as this one: http://learn.shayhowe.com/html-css/

The breadth of HTML is actually not very large, as it is not meant to include advanced features; getting acquainted on each relevant tag and attribute doesn’t take much time, because there aren’t that many. The part of HTML that is trickiest to go over is probably forms, because there are quite a few possible components (text fields, checkboxes, text areas, … even sliders and color pickers in the most recent HTML specifications!)

The promise of HTML is that you should keep your document as properly structured and semantic as you can; and if you do, it should remain easily accessible to the browsers that will exist in 20 years, while also making it easier to keep your code accessible, performant, and optimized for search engines through time. See: http://vanseodesign.com/web-design/semantic-html/

**CSS in a nutshell**

CSS (Cascading Style Sheets) were invented by Bert Bos and Håkon Wium Lie, because HTML was getting less and less semantic, and more and more about presentation, which would make it less future-proof and more verbose.

For instance, you could write that:
```
<center><p><font color="red">Hello to <b>all</b> of my visitors!</font></p></center>
```

The fact that a text should be centered, have a certain color, and be represented in bold is part of presentation, and shouldn’t be in the HTML. The fact that it’s a paragraph, however, is part of the structure, and therefore is semantic information.
Also, if you needed to make a whole page red, you needed to write ```<font color="red"> at every single line.```

CSS enforces not only semantics in the HTML, but also mutualization of the presentation layer, and therefore less code.

Now, ```<center>```, <font> and <b> are banned in HTML, and we got some more semantic tags, like <strong>, <em>, and more recently, <article>, <section>, <aside>, ...

Wondering about the difference between <strong> and <b>? –> (http://www.html-5-tutorial.com/strong-and-b-elements.htm)

## Web development tools

Before diving into your first front-end development project, you should take some time to learn to use the web development tools that are embedded into all modern browsers. Search online how to access the ones for the browser you wish to be using.

Those tools are typically more powerful than just for HTML/CSS development, and also cover JavaScript debugging, tracking HTTP requests, even some performance diagnostic tools sometimes. The HTML/CSS pane usually displays the HTML code as the browser interprets it, on the left (as a tree that you can deploy or fold back), and the CSS rules to the right, which you can edit in place. Of course, all of the edits you’re doing in there are being done in the browser’s memory. If you want to keep these changes, you’ll have to do them in your source code.

<p align="center">
  <img src="https://github.com/ghbouzrbay/AirBnB_clone/blob/master/web_static/style/web_devpp.png">
</p>



