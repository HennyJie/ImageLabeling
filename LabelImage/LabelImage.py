import os
import vtk, ctk, slicer
import sys, getopt
import argparse
import logging


def getVtkImageDataAsOpenCvMat(volumeNodeName):
  cameraVolume = slicer.util.getNode(volumeNodeName)
  image = cameraVolume.GetImageData()
  shape = list(cameraVolume.GetImageData().GetDimensions())
  shape.reverse()
  components = image.GetNumberOfScalarComponents()
  if components > 1:
    shape.append(components)
    shape.remove(1)
  imageMat = vtk.util.numpy_support.vtk_to_numpy(image.GetPointData().GetScalars()).reshape(shape)
  return imageMat


def CollectingImages():
  import numpy
  try:
    # the module is in the python path
    import cv2
  except ImportError:
    # for the build directory, load from the file
    import imp, platform
    if platform.system() == 'Windows':
        cv2File = 'cv2.pyd'
        cv2Path = '../../../../OpenCV-build/lib/Release/' + cv2File
    else:
        cv2File = 'cv2.so'
        cv2Path = '../../../../OpenCV-build/lib/' + cv2File
    scriptPath = os.path.dirname(os.path.abspath(__file__))
    cv2Path = os.path.abspath(os.path.join(scriptPath, cv2Path))
    # in the build directory, this path should exist, but in the installed extension
    # it should be in the python pat, so only use the short file name
    if not os.path.isfile(cv2Path):
        cv2Path = cv2File
    cv2 = imp.load_dynamic('cv2', cv2File)

  # imageClassName = args.class_name
  imageClassName = raw_input("input label:")
  print(imageClassName)
  # basePath = os.path.dirname(os.path.abspath(__file__))
  imageClassFilePath = os.path.join("C:\Users\hejie\Documents\ImageClassification\imageFrames", imageClassName)

  numImagesInFile = len(os.listdir(imageClassFilePath))
  print(numImagesInFile)
  # logging.info(numImagesInFile)

  imData = getVtkImageDataAsOpenCvMat('Webcam_Reference')
  imDataBGR = cv2.cvtColor(imData,cv2.COLOR_RGB2BGR)

  if numImagesInFile < 10:
    fileName = imageClassName + "_0" + str(numImagesInFile) + ".jpg"
  else:
    fileName = imageClassName + "_" + str(numImagesInFile) + '.jpg'
  cv2.imwrite(os.path.join(imageClassFilePath, fileName), imDataBGR)

  # print(os.path.join(imageClassFilePath,fileName))
  # print(imDataBGR)
  print(fileName)

# def parse_arguments(argv):
#   parser = argparse.ArgumentParser()
#   parser.add_argument('--class_name', type=str,
#                         help='class of the object appear in this frame', default='nothing')
#   return parser.parse_args(argv)


if __name__ == "__main__":
  # CollectingImages(parse_arguments(sys.argv[1:]))
  CollectingImages()


