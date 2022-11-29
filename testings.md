## Testings

This project has gone through extensive testing continuously during development, and every bug has been squashed to the best of my limited time and ability.

From the very beginning of the project, structure and security have been top priorities, and do_permissions.py is the result of that. It was not possible without extensive testing.

For every model, POST and PUT have been tested throughout the development process, and results are as expected.

![post-button](./docs/testings/post-button.webp)

![content-created](./docs/testings/content-created.webp)

The social model options have been tested and work as expected.

![social-choices](./docs/testings/socials-choices.webp)

The deletion of objects worked as expected. Only the object's owner has the ability to update and/or delete it.

![delete-button](./docs/testings/delete-button.webp)

![linktree-deleted](./docs/testings/linktree-deleted.webp)

Validation and file size

The maximum file size set for this project is 2 MB, and the user will get a notification if the image is over that.

![bad-request-file-size-validation](./docs/testings/bad-request-file-size-validation.webp)
![bad-request-image-result](./docs/testings/bad-request-image-result.webp)

Organizing files and users helps with better cleaning and ensures the app runs optimally.

![files-structure](./docs/testings/files-structure.webp)

GET-only endpoints are in place for both logged-in and not-authenticated users to ensure every user is where they should be.

![get-only](./docs/testings/get-only.webp)

![opened-endpoint-200](./docs/testings/opened-endpoints-200.webp)

Rules and limitations are set for optimal results.

![limitations-rules](./docs/testings/limitations-rules.webp)

Slug-based lookups were tested throughout the models, which worked as expected.

![slug-based-looup](./docs/testings/slug-based-look-up.webp)
