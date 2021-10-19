from PyQt5 import QtCore, QtGui, QtWidgets
from apkInfo import *
import requests

# make package size human readable
def sizeof_fmt(num, suffix='B'):
	for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
		if abs(num) < 1024.0:
			unit = ' ' + unit
			return "%3.1f%s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%.1f%s%s" % (num, ' Yi', suffix)


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 360)
		MainWindow.setToolTip("")
		MainWindow.setStyleSheet("")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.link_input = QtWidgets.QLineEdit(self.centralwidget)
		self.link_input.setGeometry(QtCore.QRect(180, 30, 441, 21))
		font = QtGui.QFont()
		font.setPointSize(8)
		font.setItalic(True)
		self.link_input.setFont(font)
		self.link_input.setAutoFillBackground(False)
		self.link_input.setText("")
		self.link_input.setFrame(True)
		self.link_input.setCursorPosition(0)
		self.link_input.setAlignment(QtCore.Qt.AlignCenter)
		self.link_input.setDragEnabled(True)
		self.link_input.setReadOnly(False)
		self.link_input.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
		self.link_input.setClearButtonEnabled(False)
		self.link_input.setObjectName("link_input")
		self.getlink = QtWidgets.QPushButton(self.centralwidget)
		self.getlink.setGeometry(QtCore.QRect(320, 100, 75, 23))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.getlink.setFont(font)
		self.getlink.setIconSize(QtCore.QSize(20, 20))
		self.getlink.setObjectName("getlink")
		self.directory = QtWidgets.QLineEdit(self.centralwidget)
		self.directory.setGeometry(QtCore.QRect(180, 60, 441, 21))
		font = QtGui.QFont()
		font.setItalic(True)
		self.directory.setFont(font)
		self.directory.setToolTip("")
		self.directory.setAutoFillBackground(False)
		self.directory.setText("")
		self.directory.setFrame(True)
		self.directory.setCursorPosition(0)
		self.directory.setAlignment(QtCore.Qt.AlignCenter)
		self.directory.setDragEnabled(True)
		self.directory.setReadOnly(False)
		self.directory.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
		self.directory.setClearButtonEnabled(False)
		self.directory.setObjectName("directory")
		self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
		self.progressBar.setEnabled(True)
		self.progressBar.setGeometry(QtCore.QRect(90, 210, 651, 23))
		font = QtGui.QFont()
		font.setPointSize(11)
		font.setBold(False)
		font.setItalic(True)
		font.setWeight(50)
		self.progressBar.setFont(font)
		self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
		self.progressBar.setStyleSheet("")
		self.progressBar.setProperty("value", 0)
		self.progressBar.setObjectName("progressBar")
		self.download0 = QtWidgets.QPushButton(self.centralwidget)
		self.download0.setGeometry(QtCore.QRect(400, 100, 75, 23))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.download0.setFont(font)
		self.download0.setIconSize(QtCore.QSize(20, 20))
		self.download0.setObjectName("download")
		self.status = QtWidgets.QLabel(self.centralwidget)
		self.status.setGeometry(QtCore.QRect(0, 260, 801, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.status.setFont(font)
		self.status.setAutoFillBackground(False)
		self.status.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.status.setFrameShadow(QtWidgets.QFrame.Plain)
		self.status.setLineWidth(5)
		self.status.setMidLineWidth(0)
		self.status.setTextFormat(QtCore.Qt.PlainText)
		self.status.setObjectName("status")
		self.developer = QtWidgets.QLabel(self.centralwidget)
		self.developer.setGeometry(QtCore.QRect(10, 310, 221, 31))
		self.developer.setFont(font)
		self.developer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.developer.setOpenExternalLinks(True)
		self.developer.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
		self.developer.setObjectName("developer")
		self.status.setAlignment(QtCore.Qt.AlignCenter)
		self.status.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(100, 170, 111, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(100, 140, 111, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(210, 140, 450, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_4.setFont(font)
		self.label_4.setMouseTracking(False)
		self.label_4.setToolTip("")
		self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
		self.label_4.setLineWidth(0)
		self.label_4.setMidLineWidth(0)
		self.label_4.setScaledContents(False)
		self.label_4.setIndent(-1)
		self.label_4.setObjectName("label_4")
		font = QtGui.QFont()
		font.setPointSize(8)
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(140, 170, 450, 31))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.label_5.setFont(font)
		self.label_5.setMouseTracking(False)
		self.label_5.setToolTip("")
		self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
		self.label_5.setLineWidth(0)
		self.label_5.setMidLineWidth(0)
		self.label_5.setScaledContents(False)
		self.label_5.setIndent(-1)
		self.label_5.setObjectName("label_5")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.retranslateUi(MainWindow)
		self.getlink.clicked.connect(self.run)
		self.download0.clicked.connect(self.down)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def run(self):
		self.status.clear()

		url = 'https://api.cafebazaar.ir'
		downloads_url = '/rest-v1/process/AppDetailsV2Request'

		# get apl url from input
		link = self.link_input.text()
		if "?" in link:
			packageName = ''.join(re.findall(r'app\/(.+)\?', link))
		else:
			packageName = ''.join(re.findall(r'app\/(.+)$', link))

		payload = {
			"properties": properties,
			"singleRequest": {
				"appDownloadInfoRequest": {
					"downloadStatus": 1,
					"packageName": packageName,
					"referrers": [{
						"type": 11,
						"extraJson": "{\"services\":\"vitrin\",\"slug\":\"home\"}"
					}, {
						"type": 1,
						"extraJson": "{\"services\":\"vitrin\",\"index\":2,\"title\":\"برنامه‌های پیشنهادی برای شما\",\"source\":\"recom\",\"is_shuffled\":false,\"referrer_identifier\":\"external_Recommended Apps For You\"}"
					}, {
						"type": 2,
						"extraJson": "{\"services\":\"vitrin\",\"index\":2,\"referrer_identifier\":\"\"}"
					}, {
						"type": 17,
						"extraJson": "{\"package_name\":\"ir.mci.ecareapp\",\"service\":\"sejel\"}"
					}
					]
				}
			}
		}

		# get apk info
		http = urllib3.PoolManager()
		encoded_data = json.dumps(payload).encode('utf-8')

		r = http.request('POST', url + downloads_url, body = encoded_data)
		app.processEvents()

		response = json.loads(r.data.decode('utf-8'))
		if response['properties']['statusCode'] == 200:
			prefix = response['singleReply']['appDownloadInfoReply']
			cdn = prefix['cdnPrefix'][0]
			app_token = prefix['token']
			packageSize = prefix['packageSize']
			url = cdn + 'apks/' + app_token + '.apk'
			app.processEvents()
			# set apk url and package size
			self.label_4.setText(str(app_detail(packageName, link)).strip())
			self.label_5.setText(sizeof_fmt(int(packageSize)))
			app.processEvents()
			self.status.setText(url)
		else:
			app.processEvents()
			self.status.setText("Connection failed!")
	
	# apk download function
	def down(self):
		self.status.clear()
		self.status.setText("working...")
		url = 'https://api.cafebazaar.ir'
		downloads_url = '/rest-v1/process/AppDetailsV2Request'

		link = self.link_input.text()
		if "?" in link:
			packageName = ''.join(re.findall(r'app\/(.+)\?', link))
		else:
			packageName = ''.join(re.findall(r'app\/(.+)$', link))

		payload = {
			"properties": properties,
			"singleRequest": {
				"appDownloadInfoRequest": {
					"downloadStatus": 1,
					"packageName": packageName,
					"referrers": [{
						"type": 11,
						"extraJson": "{\"services\":\"vitrin\",\"slug\":\"home\"}"
					}, {
						"type": 1,
						"extraJson": "{\"services\":\"vitrin\",\"index\":2,\"title\":\"برنامه‌های پیشنهادی برای شما\",\"source\":\"recom\",\"is_shuffled\":false,\"referrer_identifier\":\"external_Recommended Apps For You\"}"
					}, {
						"type": 2,
						"extraJson": "{\"services\":\"vitrin\",\"index\":2,\"referrer_identifier\":\"\"}"
					}, {
						"type": 17,
						"extraJson": "{\"package_name\":\"ir.mci.ecareapp\",\"service\":\"sejel\"}"
					}
					]
				}
			}
		}

		http = urllib3.PoolManager()
		encoded_data = json.dumps(payload).encode('utf-8')

		# get download url
		r = http.request('POST', url + downloads_url, body=encoded_data)
		app.processEvents()
		response = json.loads(r.data.decode('utf-8'))
		if response['properties']['statusCode'] == 200:
			prefix = response['singleReply']['appDownloadInfoReply']
			cdn = prefix['cdnPrefix'][0]
			app_token = prefix['token']
			packageSize = prefix['packageSize']
			url = cdn + 'apks/' + app_token + '.apk'
			app.processEvents()
			self.label_4.setText(str(app_detail(packageName, link)).strip())
			self.label_5.setText(sizeof_fmt(int(packageSize)))
			#app.processEvents()
			with open(self.directory.text() + str(app_detail(packageName, link)).strip() + '.apk', "wb") as f:
				app.processEvents()
				response = requests.get(url, stream=True)
				total_length = response.headers.get('content-length')
				#app.processEvents()
				if total_length is None:  # no content length header
					f.write(response.content)
					app.processEvents()
				else:
					app.processEvents()
					dl = 0
					total_length = int(total_length)
					#app.processEvents()
					for data in response.iter_content(chunk_size=4096):
						app.processEvents()
						dl += len(data)
						f.write(data)
						done = int(100 * dl / total_length)
						self.progressBar.setValue(done)
						
					if done == 100:
						self.status.clear()
						self.status.setText("Done")
		else:
			app.processEvents()
			self.status.setText("Connection failed!")
			

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "CafeBazaar Downloader"))
		self.link_input.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">example https://cafebazaar.ir/app/package_name</p></body></html>"))
		self.link_input.setPlaceholderText(_translate("MainWindow", "YOUR APPLICATION LINK"))
		self.getlink.setText(_translate("MainWindow", "Get link"))
		self.directory.setPlaceholderText(_translate("MainWindow", "ENTER YOUR SAVING DIRECTORY"))
		self.download0.setText(_translate("MainWindow", "Download"))
		self.status.setText(_translate("MainWindow", ""))
		self.label_2.setText(_translate("MainWindow", "Size: "))
		self.label.setText(_translate("MainWindow", "Package name: "))
		self.label_4.setText(_translate("MainWindow", ""))
		self.label_5.setText(_translate("MainWindow", ""))
		self.developer.setText(_translate("MainWindow", "<html><head/><body><a href=\'https://github.com/mohamadkhalaj/\'>Developed By MohammadKhalaj</a></body></html>"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
