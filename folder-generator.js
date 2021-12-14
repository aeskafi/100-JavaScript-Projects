// const { resolve } = require('path'),
//     { readdir } = require('fs').promises;

// async function getFiles(dir) {
//     const dirents = await readdir(dir, { withFileTypes: true });
//     const files = await Promise.all(dirents.map((dirent) => {
//         const res = resolve(dir, dirent.name);
//         // return dirent.isDirectory() ? getFiles(res) : res;
//         return res;
//     }));
//     return Array.prototype.concat(...files);
// }

// const directory = "./";

// getFiles(directory).then(results => {
//     const html = `<ul>` +
//         results.map(fileOrDirectory => `<li>${fileOrDirectory}</li>`).join('\n') +
//         `</ul>`;

//     process.stdout.write(html);
//     // or you could use something like fs.writeFile to write the file directly
// });
var ignoreList = ['.git'];
var html = ``;

var fs = require("fs"),
    path = require("path");

var p = "./"
var links = "";

fs.readdir(p, function (err, files) {
    if (err) {
        throw err;
    }

    files.map(function (file) {
        return path.join(p, file);
    }).filter(function (file) {
        return fs.statSync(file).isDirectory();
    }).forEach(function (dir) {
        //  console.log("%s", dir, path.extname(dir));
        !ignoreList.includes(dir) && process.stdout.write(`
            <article class="flex m-2 items-center">
                <img src="https://img.icons8.com/color/24/000000/folder-invoices--v1.png" />
                <a class="pl-2 font-light font-mono text-sm"
                    href="${dir}">${dir}</a>
            </article>
        `);
    });
    process.stdout.write(`</section>
</body>
</html>`);
});

process.stdout.write(`
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Folder List</title>
</head>

<body class="flex flex-1 bg-slate-300 min-h-screen align-center justify-center">
    <section class="flex-1 bg-white rounded shadow-2xl max-h-full mx-3 my-3">`);

// process.stdout.write(html);
