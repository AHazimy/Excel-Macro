import cv2


#To read image i have to import cv2 then
# X = cv2.imread("Path_of_image", 0) >>> 0 for reading in gray and black and white 
# X = cv2.imread("Path_of_image", 1) >>> 1 for reading in BGR blue and green and red
#and we have arrays that present the degree of colors of each pixel
# example from jupyter: im_g=cv2.imread("smallgray.png",0)


#To create image i have to use cv2.imwrite() methode:
# cv2.imwrite("Path_and_Name_of_new_image_from_my_choice", X) >>> when X is an array present color degrees of each pixel in the image ex:
# cv2.imwrite(r"C:\Users\AlyGh\Desktop\Python_mega_course\Application\new_COD.png", im_g)


#Slicing list is like choose some values from this list by they indexes ex:
# a = [] >>> slicing is: a[0:2] or a[1:4] .....


#To access a sepcific index in array we use slicing like that:
# a[2:4 , 3:4] 2:4 for indexing the rows and 3:4 for indexing the columns 

#array.shape is like the resolution of a picture ex about COD.png: im_g.shape >>> (2160, 3840)
#array.flat transfer the array to vertical one column


#To merge 2 or more arrays we use numpy.hstack(()) for horizontal stacking
#and numpy.vstack(()) for vertical stacking 
# but this 2 methodes take just one argument so for that i insert (()) 
# ex: ims = numpuy.vstack((im_g, im_g, im_g))


#For split array we use lst = numpy.hsplit(im_g, x) >>>when x is the number of split part 
#and lst = numpy.vsplit(im_g, x) for vertical split
#and here "lst" is a list of arrays