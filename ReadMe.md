# REACT JS Learning Notes

## References
* [Online Documents](https://create-react-app.dev/docs/getting-started)
* [Home Page](https://reactjs.org/)
* [Getting started](https://reactjs.org/docs/getting-started.html)

## Start from scratch
```
sudo npx create-react-app wang-app
sudo chown -R wangqianjiang wang-app
cd wang-app
npm start
```
You need change ownership for all all files under the wang-app folder because you need make change on those source code. where 'wangqianjiang' is owner of my laptop.

## Install pip
```sh
phthon3 get-pip.py
```

## Install UI
```
npm i semantic-ui-react semantic-ui-css 
```
add the followin line in index.js
```js
import 'semantic-ui-css/semantic.main.css'
```

add oneline in package.json
```json
  "eslintConfig": {
    "extends": "react-app"
  },
  "proxy":"http://localhost:5000",
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
```