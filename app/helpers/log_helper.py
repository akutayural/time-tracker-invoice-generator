import json

from app import request_logger


class RequestsLogger:
    def log(self, r, class_name):
        log_data = {"request": {"url": r.request.url,
                                "method": r.request.method,
                                "body": r.request.body.decode() if isinstance(r.request.body, bytes) else r.request.body},
                    "response": {"status_code": r.status_code,
                                 "text": r.text}}
        try:
            request_logger.info(class_name + " > request: " + json.dumps(log_data))
        except Exception as e:
            log_data["request"]["body"] = None
            request_logger.info(class_name + " > request: " + json.dumps(log_data))

    def log_request(self, request, request_body, request_id):
        log_data = {"request": {"url": str(request.url),
                                "method": request.method,
                                "content_type": request.headers.get("content-type", None),
                                "body": request_body}}
        request_logger.info(request_id + " > request: " + json.dumps(log_data))

    def log_response(self, response, request_id):
        log_data = {"response": {"status_code": response.status_code,
                                 "text": response.body.decode()}}
        request_logger.info(request_id + " > response: " + json.dumps(log_data))
