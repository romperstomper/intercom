"""Test for weblog_helper."""

import logging
import mock
import unittest
import weblog_helper

LOGFILE1=[
'178.93.28.59 - - [02/Jun/2015:17:06:06 -0700] "GET /logs/access_150122.log HTTP/1.1" 200 3240056 "http://fruit.fm/20487/blog/1327873/" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36" "redlug.com"'
]
LOGFILE2=[
'180.76.15.135 - - [02/Jun/2015:17:05:23 -0700] "GET /logs/access_140730.log HTTP/1.1" 200 979626 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"',
'180.76.15.137 - - [02/Jun/2015:17:05:28 -0700] "GET /logs/access_140730.log HTTP/1.1" 200 7849856 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"',
'180.76.15.17 - - [02/Jun/2015:17:20:23 -0700] "GET /logs/access_141026.log HTTP/1.1" 200 45768 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)" "www.redlug.com"'
]

class TestAWeblogHelper(unittest.TestCase):
  def setUp(self):
    self.testip1 = '178.93.28.59'
    self.testip2 = '178.93.28.52'
    self.testcidr1 = '180.76.15.0/24'
    self.testcidr2 = '180.76.15.0/32'
    
  @mock.patch('__builtin__.open')
  def test_parselog_single_ip_pass(self, mock_open):
    context_manager = mock.Mock()
    mock_open.return_value = context_manager
    enter_mock = mock.Mock()
    enter_mock.return_value = LOGFILE1
    exit_mock = mock.Mock()
    context_manager.__enter__ = enter_mock
    context_manager.__exit__ = exit_mock
    expected = LOGFILE1
    result = weblog_helper.parselog(self.testip1, logfile=LOGFILE1)
    self.assertEqual(expected, result)

  @mock.patch('__builtin__.open')
  def test_parselog_single_ip_fail(self, mock_open):
    context_manager = mock.Mock()
    mock_open.return_value = context_manager
    enter_mock = mock.Mock()
    enter_mock.return_value = LOGFILE1
    exit_mock = mock.Mock()
    context_manager.__enter__ = enter_mock
    context_manager.__exit__ = exit_mock
    expected = LOGFILE1
    result = weblog_helper.parselog(self.testip2, logfile=LOGFILE1)
    self.assertNotEqual(expected, result)

  @mock.patch('__builtin__.open')
  def test_parselog_ip_set_pass(self, mock_open):
    context_manager = mock.Mock()
    mock_open.return_value = context_manager
    enter_mock = mock.Mock()
    enter_mock.return_value = LOGFILE2
    exit_mock = mock.Mock()
    context_manager.__enter__ = enter_mock
    context_manager.__exit__ = exit_mock
    expected = LOGFILE2
    result = weblog_helper.parselog(self.testcidr1, logfile=LOGFILE2)
    self.assertEqual(expected, result)

  @mock.patch('__builtin__.open')
  def test_parselog_ip_set_fail(self, mock_open):
    context_manager = mock.Mock()
    mock_open.return_value = context_manager
    enter_mock = mock.Mock()
    enter_mock.return_value = LOGFILE2
    exit_mock = mock.Mock()
    context_manager.__enter__ = enter_mock
    context_manager.__exit__ = exit_mock
    expected = LOGFILE1
    result = weblog_helper.parselog(self.testcidr1, logfile=LOGFILE1)
    self.assertNotEqual(expected, result)

if __name__ == '__main__':
  unittest.main()
