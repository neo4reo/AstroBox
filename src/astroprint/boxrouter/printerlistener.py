# coding=utf-8
__author__ = "Daniel Arroyo. 3DaGogo, Inc <daniel@3dagogo.com>"
__license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'

import json
import logging

class PrinterListener(object):
	def __init__(self, socket):
		self._logger = logging.getLogger(__name__)
		self._socket = socket
		self._lastSent = {
			'temp_update': None
		}

	def sendHistoryData(self, data):
		pass

	def addTemperature(self, data):
		payload = {
			'bed': { 'actual': data['bed']['actual'], 'target': data['bed']['target'] },
			'tool0': { 'actual': data['tool0']['actual'], 'target': data['tool0']['target'] }
		}

		if self._lastSent['temp_update'] != payload:
			try:
				self._socket.send(json.dumps({
					'type': 'temp_update',
					'data': payload
				}))

				self._lastSent['temp_update'] = payload

			except Exception as e:
				self._logger.error('Error sending [temp_update] event: %s' % e)

	def addLog(self, data):
		pass

	def addMessage(self, data):
		pass

	def sendCurrentData(self, data):
		pass

	def sendEvent(self, type):
		pass

	def sendFeedbackCommandOutput(self, name, output):
		pass