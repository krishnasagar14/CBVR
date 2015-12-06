#################################################################################################
### Program: Frame Extraction from a Input video. ###
### Author: Krishnasagar Subhedarpage (pagesagar@gmail.com) ###
### Date: 13/11/2014 ###
#################################################################################################

#################################################################################################
### Defination: To extract frames from videos. Extraction simply done with frame frequecy of defined value(can be altered).###
### Inputs: v_name - variable to receive input video file name. Default value: None. ###
###         op_dir - variable to receive output directory name. Default value: 'frames'. ###
### Output: frames saved into "frames" directory in sequencial number convention. ###
#################################################################################################
def fev(v_name = None, op_dir = 'frames'):
    import cv2
    import os
    if v_name != None:
        if os.path.isfile(v_name) == True:
            # to capture video from a source
            cap_var = cv2.VideoCapture(v_name)
            #to set frame id
            img_no=1
            #to set frame frequency property in video capture
            no_frame = cap_var.get(7)
            ff = 100
            #to set frames directory
            if os.path.isdir(op_dir) == False:
                os.mkdir(op_dir)
            while img_no <= no_frame:
                for x in range(0,ff):
                    r,f = cap_var.read()
                    if r == False:
                        break
                r_val, frame = cap_var.read()
                if r_val == False:
                    break
                cv2.imwrite('frames/' + str(img_no) + '.jpeg',frame)
                img_no = img_no + 1
                if img_no > no_frame:
                    break
            else:
                cap_var.release()
        else:
            print '\nPlease check file name. Please fill in existing video file.'
    else:
        print '\nPlease fill in correct video file name. Use fev.fev(<video_name>)'
