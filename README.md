# prompt-be
This is a `Python / Django` project.

## Getting Started

First, run the development server:

```bash
# insert script call
```

The following log message should be displayed in console output:

```bash
# insert output
```

> Note!! If the schema was updated, run the following command to apply the updated changes: `insert script call`

Visit `insert test route e.g http://localhost:3000/user` in your browser just to confirm routes are configured and working properly. If all is working properly, you should get the below response on browser.

```python
# insert test response
```

## Environmental Variable

Create a .env file inside the root of your application and include the following content:

```bash
# insert env variables
```

> Note!! you need to create the database `prompt` yourself before doing any other thing within the app if you need it to work properly. You could use tool like `PgAdmin`

# Routes

Explain routes file structure

```python
# Insert code template
```

> `Do Not Touch the Base file within the controller directory. It should only be inherited from.`

# Commit Standards

## Branches

- **dev** -> pr this branch for everything `backend` related
- **main** -> **dont touch** this branch, this is what is running in production.

## Contributions

Prompt is open to contributions, but I recommend creating an issue or replying in a comment to let us know what you are working on first that way we don't overwrite each other.

## Contribution Guidelines

1. Clone the repo `git clone https://github.com/hslcreators/prompt-be`.
2. Open your terminal & set the origin branch: `git remote add origin https://github.com/hslcreators/prompt-be.web.git`
3. Pull origin `git pull origin dev`
4. Create a new branch for the task you were assigned to, eg : `git checkout -b feat-file-parser`
5. After making changes, do `git add .`
6. Commit your changes with a descriptive commit message : `git commit -m "your commit message"`.
7. To make sure there are no conflicts, run `git pull upstream dev`.
8. Push changes to your new branch, run `git push -u origin feat-file-parser`.
9. Create a pull request to the `dev` branch not `main`.
10. Ensure to describe your pull request.
11. > If you've added code that should be tested, add some test examples.

### _Commit CheatSheet_

| Type     |                          | Description                                                                                                 |
| -------- | ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| feat     | Features                 | A new feature                                                                                               |
| fix      | Bug Fixes                | A bug fix                                                                                                   |
| docs     | Documentation            | Documentation only changes                                                                                  |
| style    | Styles                   | Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)      |
| refactor | Code Refactoring         | A code change that neither fixes a bug nor adds a feature                                                   |
| perf     | Performance Improvements | A code change that improves performance                                                                     |
| test     | Tests                    | Adding missing tests or correcting existing tests                                                           |
| build    | Builds                   | Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)         |
| ci       | Continuous Integrations  | Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs) |
| chore    | Chores                   | Other changes that don't modify backend, frontend or test files                                             |
| revert   | Reverts                  | Reverts a previous commit                                                                                   |

> _Sample Commit Messages_

- `chore: Updated README file` := `chore` is used because the commit didn't make any changes to the backend, frontend or test folders in any way.
- `feat: Added plugin info endpoints` := `feat` is used here because the feature was non-existent before the commit.
