# Contributing to Dwarf Game

## Q: What kinds of contributions do you want?

A: All kinds of contributions are welcome! We're looking for people to help with the following:

-   **Frontend**: TypeScript (Angular) with SCSS. We're using Angular because it's easy to write and we can reuse components.
-   **Backend**: Python (FastAPI). We're using FastAPI because Python is simple to write and FastAPI is very fast.
-   **Database**: We're using PostgreSQL for the database, but FastAPI makes it easy to switch to a different database if we need to. We also have PyDantic models for the database tables so we really don't have to write much SQL.
-   **Artwork**: We need artwork for the game. If you're an artist, we'd love to have your help!

## Q: How do I contribute?

### A: Reporting Bugs

If you find a bug, please report it! We want to know about bugs so we can fix them. Please follow these steps to report a bug:

1. Go to the Issues tab on GitHub
2. Click the "New Issue" button
3. Click the "Get Started" button under "Bug Report"
4. Fill out the form and click "Submit New Issue"

### A: Suggest Enhancements

If you have an idea for the game, please let us know!

### A: Contribute Code\*

This game is open source, so you can contribute code to it! Please follow these steps to contribute code:

1. Fork the repository
2. Make your changes
3. Submit a pull request

#### \*Contribution Guidelines

Please follow these guidelines when contributing code:

-   **Code Style**: Please follow the code style of the project. We're using [Prettier](https://prettier.io/) to format our code. This helps keep the code consistent and makes it easier to read, and won't trigger insane diffs in pull requests.
-   **Documentation**: Please document your code. For FastAPI, it has built-in docs using [SwaggerUI](https://github.com/swagger-api/swagger-ui). For Angular, we haven't decided on a documentation tool yet.
-   **Commit Messages**: Please write good commit messages.
-   **Pull Requests**: Please make sure your pull request is up-to-date with the latest changes in the main branch.
-   **Making Changes to Game Mechanics**: If you're making changes to core game mechanics, please make sure to discuss it with the team first - of course, you can still submit a pull request, but we want to make sure we're all on the same page.
-   **Read the license**: Please read the license before contributing. We want to make sure that your contributions are compatible with the license.

## Licensing

-   **License (for code)**: We are currently using the [GNU GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license for code. Please make sure your code is compatible with this license. There are further details in the [LICENSE](license.md) file.
-   **License (for art)**: We are currently using a custom license for art. Please see the bottom of [LICENSE](license.md) for details. In essence, we want to make sure that artists retain their rights to their art, but that we can use the art in the game without worrying about the artist revoking their permission.
