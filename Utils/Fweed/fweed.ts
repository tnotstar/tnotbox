// Copyright (c) 2022, Antonio Alvarado Hernández

import { config } from './deps.ts';

interface Keys {
    consumerKey: string,
    consumerSecret: string,
    accessToken: string,
    accessSecret: string,
}

class UpstreamService {
    private consumerKey: string;
    private consumerSecret: string;
    private accessToken: string;
    private accessSecret: string;

    constructor(keys: Keys) {
        this.consumerKey = keys.consumerKey;
        this.consumerSecret = keys.consumerSecret;
        this.accessToken = keys.accessToken;
        this.accessSecret = keys.accessSecret;
    }
}

const main = async () => {
    const myUpstreamKeys = {
        consumerKey: 'a', //Deno.env.get('FWEED_UPSTREAM_CONSUMER_KEY'),
        consumerSecret: 'b', //Deno.env.get('FWEED_UPSTREAM_CONSUMER_SECRET'),
        accessToken: 'xx',
        accessSecret: 'yy',
    }
    const upstream = new UpstreamService(myUpstreamKeys);
}

config({ export: true });
main();
const dale: string = Deno.env.get('FWEED_UPSTREAM_CONSUMER_KEY')?;
console.log(dale);

// EOF
