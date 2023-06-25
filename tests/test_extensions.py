from unittest.mock import Mock

def assert_not_called_with(self, *args, **kwargs):
    try:
        self.assert_called_with(*args, **kwargs)
    except AssertionError:
        return
    raise AssertionError('Expected %s to not have been called.' % self._format_mock_call_signature(args, kwargs))

Mock.assert_not_called_with = assert_not_called_with