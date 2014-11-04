#!/bin/sh
':' //; exec `command -v nodejs || command -v node || command -v js` "$0" "$@"

var r = require("rethinkdb");

r.connect({host: "localhost", port: 28015}, function(err, conn) {
    if(err) throw err;

    r.db("test").tableCreate("tv_shows").run(conn, function(err, res) {
        if(err) throw err;

        r.table("tv_shows").insert([
            {name: "Star Trek TNG", episodes: 148},
            {name: "Battlestar Galactica", episodes: 78},
        ]).run(conn, function(err, res) {
            console.log("Results:", res);
            conn.close();
        });
    });
});

// EOF
