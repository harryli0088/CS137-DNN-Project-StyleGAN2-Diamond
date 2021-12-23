# create-svelte

Everything you need to build a Svelte project, powered by [`create-svelte`](https://github.com/sveltejs/kit/tree/master/packages/create-svelte);

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```bash
# create a new project in the current directory
npm init svelte@next

# create a new project in my-app
npm init svelte@next my-app
```

> Note: the `@next` is temporary

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

Before creating a production version of your app, install an [adapter](https://kit.svelte.dev/docs#adapters) for your target environment. Then:

```bash
npm run build
```

> You can preview the built app with `npm run preview`, regardless of whether you installed an adapter. This should _not_ be used to serve your app in production.



## Deploying to Github Pages

Adapted from https://github.com/Sh031224/svelte-kit-github-page-example

1. Install ```adapter-static``` and ```gh-pages```
```
npm i -D @sveltejs/adapter-static@next gh-pages
```

2. Updated ```svelte.config.js```
```js
import static_adapter from '@sveltejs/adapter-static';

const config = {
  kit: {
    adapter: static_adapter({
      // default options are shown
      pages: 'build',
      assets: 'build',
      fallback: null
    }),
    paths: {
      base: process.env.NODE_ENV==="production" ? '/your-repo-name' : undefined,
    }
  }
};

export default config;
```

3. Add an empty ```.nojekyll``` file in your ```static/``` directory, otherwise GitHub Pages will ignore files with a leading underscore (ie ```_app/```)

4. Add a deploy script to ```package.json```
```json
{
  "scripts": {
    "deploy": "npm run build && npx gh-pages -d build -t true"
  }
}
```

5. Run the deploy script
```
npm run deploy
```
