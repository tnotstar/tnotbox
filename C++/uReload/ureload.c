#include <stdio.h>

#include "uv.h"

int
make_request() {
	printf("Making request...\n");
	return 0;
}

static uv_tcp_t server;

int
main (void) {

	struct sockaddr_in address;
	int rs;

	/* always initializes */
	uv_init();

	/* set up some servers */
	uv_tcp_init(&server, NULL, NULL);

	address = uv_ip4_addr("0.0.0.0", 8888);
	rs = uv_bind(&server, address);
	if (rs) {
		uv_err_t err = uv_last_error();
		printf("bind: %s\n", uv_strerror(err);
		return -1;
	}
	
	rs = uv_listen(&server, 128, on_connect);
	if (rs) {
		uv_err_t err = uv_last_error();
		printf("listen: %s\n", uv_strerror(err);
		return -1;
	}

	/* run mainloop */
	uv_run();
	return 0;
}

/* EOF */
