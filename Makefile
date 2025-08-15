CHECK_PYTHON = $(shell which python3 || echo "python3_not_found")

all: ipv4chat

ipv4chat: ipv4chat.py
	@if [ "$(CHECK_PYTHON)" = "python3_not_found" ]; then \
		echo "Error: python3 not found. Install it first."; \
		exit 1; \
	fi
	chmod +x ipv4chat.py
	cp ipv4chat.py ipv4chat  

clean:
	rm -f ipv4chat dummy

install: ipv4chat
	cp ipv4chat /usr/local/bin/

uninstall:
	rm -f /usr/local/bin/ipv4chat

.PHONY: all clean install uninstall 
