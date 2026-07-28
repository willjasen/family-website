# family-website

This repo contains the website export from MacFamilyTree for a family tree kept up by me. I began this tree using information from [http://tombuchanan.net](http://tombuchanan.net)

This website gets deployed to [https://family.willjasen.com](https://family.willjasen.com)

After exporting a new MacFamilyTree site into `tree/`, run:

```sh
python3 add_footer.py
```

This refreshes the Google Analytics snippet in the exported HTML and tracks
hash-based navigation between pages in the family-tree app.
