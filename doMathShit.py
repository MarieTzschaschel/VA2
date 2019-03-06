import TimeLabelDataModule
from TimeLabelDataSetModule import TimeLabelDataSet as TDLS 

pfad = "C:\\Users\\Marie\\Desktop\\VoiceAnalysis\\2019-03-06\\16-1"

dataSet = TDLS()
dataSet.importFromFile(pfad)
#dataSet.printData()
timeLabel = dataSet.dataSets[0]
pauses = timeLabel.SoundToPauses()
print("pauses ",pauses)
timeLabel.getPauseLengths()
PauseLengths = sorted(timeLabel.pauseLengths)
print("pause Lengths ", PauseLengths)
avgSilDur = timeLabel.getAvgSilDur()
print("avgSilDur ",avgSilDur)
mPause = timeLabel.getmedianPause()
print("Median Pause ",mPause)
StandardDev = timeLabel.getStandardDevPauses()
print("StandardDev ",StandardDev)
