# Chapter 9: Asynchronous Calls to Web Services

*From TN-CustomChartsReports*

---

## Overview

In Empower 3.6.3.54 and later, it is possible to make asynchronous calls to local or remote web services from the JavaScript that defines a custom chart or report. This provides Adaptive Touch capabilities to custom client-side charts and reports, but uses existing web services and allows the chart or report itself to be defined entirely on the client side.

## Making Asynchronous Service Calls

To make an asynchronous call to a local or remote web service, include code like the following somewhere in the anonymous function defining your custom chart or report:

```javascript
if (extra.lines) {
  lines = extra.lines;
} else {
  var svc = 'https://dev.encore-analytics.com/dev-empower/vcd.cgi';
  s = svc + encodeURIComponent('?projectName=' +
    args.cc + '&WBS=' + args.ce);

  var ret = {
    "url": s,
    "name": "lines"
  };

  return JSON.stringify(ret);
}
```

The code checks first for the existence of a specified object in the default `extra` object. If not found, the code returns a JSON object defining a call to a local or remote web service (with any necessary parameters), and a name to be assigned to the data returned from the service (in this case, `'lines'`).

Empower will call the service and inject the result into the `extra` object under the name provided. Note that the anonymous function is called (at least) twice. On the first call, the named object will be undefined, signaling the code to return a request for the object; on the next call, that object will be available for use.

## Important Considerations

- **Multiple service calls**: Multiple service calls may be made by assigning their results to different names. The report or chart JavaScript code would simply keep returning service requests to Empower until all the required data had been gathered, before finally returning the report HTML or chart JSON as usual.

- **Data format**: The remote service should return data in a text-based format such as JSON, XML, HTML, or plain text. If the returned text is not a JSON string, it will be stored line-by-line in a JSON array.

- **CORS support**: Remote services should support Cross-Origin Resource Sharing. See https://enable-cors.org for details.

- **Authentication**: Remote services should allow anonymous access, or be configured to allow access to the service account under which Empower is running.

## Additional Resources

The "Who Charged AT" sample chart and report have also been implemented using client-side calls to a remote web service as discussed here, and are available on request or from Empower's Freshdesk support portal.
