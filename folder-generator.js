var ignoreList = ['.git'];
var repoTitle = '100 JavaScript Projects';

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
    <title>${repoTitle}</title>
</head>

<body class="flex flex-1 bg-slate-300 min-h-screen align-center justify-center">
    <section class="flex-1 bg-white rounded shadow-2xl max-h-full mx-3 my-3">
    <h1 class="text-3xl drop-shadow-md text-center py-2 border-b-4 border-gray-500">${repoTitle}</h1>`);
