import fs from 'fs';

class Config {
	constructor(env) {
		const config = this.config();
		return config[env];
	}

	config() {
		return {
			local: {
				server: 'http://localhost:3030'
			},
			staging: {
				server: 'https://schul.tech:3030'
			},
			production: {
				server: 'http://localhost:8080'
			}
		};
	}
}

export default new Config(process.env.ENV);
