# returnsuite-website

The landing website for [ReturnSuite](https://returnsuite.com). Contains product
information, contact, terms, privacy, blog, course and documentation.


## Development

### Adding a blog post

1) Preparing the assets
   1) Create an image directory for the post at `resources/img/yyyy-MM-dd`.
   2) Copy the images and related assets as lossless files to the directory.
      Suffix them as `-original`.
   3) Run the images through a compression tool to webm unless they are a `.gif`
      or `.svg`. A great tool is [Squoosh.app](https://squoosh.app/editor). Set
      compression to `WebP`, effort to max (6) and quality to 75%. The
      compressed images should not have the `-original` suffix.
2) Creating the post
   1) Copy a similar post from `templates/blog` to a new file and name
      accordingly.
   2) Update the content and image urls to the added files.
3) Create the post metadata
   1) Add a new record to `routes/posts.json` for the new blog post.
4) Check the website and content by running the `main` python file.
5) Run all tests to ensure the images load. Right click `tests` and press run.
6) If everything passes, commit the changes to the main branch in version
   control.

Note*: Be careful using third party widgets (iframes) as they may break GDPR
compliance.


### Updating landing page images

The landing page images are generated via html+css at `/landing-images`. Editing
the javascript allows screenshots to be downloaded for use on the landing page.


### SEO, accessibility, security and performance checks

Test the pages using [PageSpeed Insights](https://pagespeed.web.dev). The
website should pass with minimal warnings and a high performance score in all
categories (green).


### GDPR Compliance check

Perform a site wide GDPR compliance check using [2GDPR](https://2gdpr.com/).
This should pass cleanly if the site isin accordance with the EU's General Data
Protection Regulation. This is required because the site offers its services
to EU members.
