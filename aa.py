import cv2

cap = cv2.VideoCapture(0)

#for image_path in TEST_IMAGE_PATHS:
 #     image = Image.open("")
  #   image_np = load_image_into_numpy_array(image)
while True:
      ret, image_np = cap.read()
     # plt.figure(figsize=IMAGE_SIZE)
     # plt.imshow(image_np)
     # plt.show()

      cv2.imshow('object detection', cv2.resize(image_np, (800,600)))
      if cv2.waitKey(25) & 0xFF == ord('q'):
         cv2.destroyAllWindows()
         break
