// An example of the use of: https://v8.dev/docs/stack-trace-api

'use strict';

function myErrorHandler(err) {
	const savedPrepareStackTrace = Error.prepareStackTrace;
	Error.prepareStackTrace = (_, stack) => stack;
	Error.captureStackTrace(new Error, myErrorHandler);
	const structuredStackTrace = err.stack;
	Error.prepareStackTrace = savedPrepareStackTrace;
	const callee = structuredStackTrace[0]?.getFunctionName()
		|| structuredStackTrace[0]?.getMethodName()
		|| structuredStackTrace[0]?.getFileName() + ':' + structuredStackTrace[0]?.getLineNumber();
	
	console.log(`myErrorHandler(${err}): called from "${callee}"...`);
}

function foo() {
	bar();
}

function bar() {
	throw new Error('This is my custom error');
}

(() => {
	try {
		foo();
	} catch (err) {
		myErrorHandler(err);
	}
})();
