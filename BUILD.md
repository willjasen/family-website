# Building the website

After exporting a new MacFamilyTree site into `tree/`, run:

```sh
./build.sh
```

The build script refreshes the Google Analytics snippet in every exported HTML
file and verifies that `tree/index.html` contains exactly one managed analytics
block. The tag tracks hash-based navigation between pages in the family-tree
app.
