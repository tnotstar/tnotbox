#!/bin/sh
':' //; exec `command -v nodejs || command -v node || command -v js` "$0" "$@"

try {
    throw new Error('hello...');
} catch (error) {
    console.error(`ey: ${error}`);
} finally {
    console.log('...goodbye!');
}

(async () => {
    const promise = new Promise((resolve, reject) => {
        if (Math.random() < 0.5)
            resolve('Hello, world!');
        else
            reject(new Error('Oops: something\'s wrong'))
    });

    await promise
        .then(results => {
            console.log(results);
            return results;
        })
        .catch(error => {
            console.error(error);
        })
        .finally(() => {
            console.log('chao..!!!');
        });
})();

// EOF
