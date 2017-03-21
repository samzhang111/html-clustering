# Clustering HTML documents through suffix-tree similarity

The goal behind this project is to implement a measure of _structural_ similarities across, well, structured documents, such as HTML. I've seen projects related to diff-ing JSON before, but I haven't had quite found an implementation to my liking. The purpose is to classify "sections" of a crawled website automatically by identifying common structures across those sections.

We consider several facts about diffing trees:
* The hierarchy of the structure is often only locally similar -- a sidebar may be shared across web pages, for example.
* Elements of similarity may be repeated -- a sidebar may expand with subcategories when a link is clicked.
* Local elements, such as React components, may be easier to identify as repetitions, than large page-level elements.

The approach currently worked on is the use of suffix trees (tries) to deduplicate the repetitive structures. It doesn't handle additions or removals, but the hope is that it will be successful enough toward the leafs that there won't be that many additions or removals to consider.

I've seen a few papers that touch on this topic, but I'm not brain enough to brain them, so if you have any resources feel free to send them my way :).
