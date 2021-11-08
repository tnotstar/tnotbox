#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase, main, mock


MESSAGE_TEXT = "Hello, world!"


def foobar(client, message):
    client.send(message)


class TestFoobar(TestCase):
    def test_foobar(self):
        mock_client = mock.Mock()
        foobar(mock_client, MESSAGE_TEXT)
        mock_client.send.assert_called_with(MESSAGE_TEXT)


if __name__ == "__main__":
    main()

# EOF
