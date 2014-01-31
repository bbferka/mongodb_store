#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import ros_datacentre_msgs.srv as dc_srv
import ros_datacentre.util as dc_util
from ros_datacentre.message_store import MessageStoreProxy
from geometry_msgs.msg import Pose, Point, Quaternion
import StringIO


if __name__ == '__main__':
    rospy.init_node("example_message_store_client")


    msg_store = MessageStoreProxy()

    p = Pose(Point(0, 1, 2), Quaternion(3, 4,  5, 6))
    p2 = Pose()
    meta = {'also':'bob'}

    try:
        msg_store.insert_named("nice pose", p, meta)
        msg_store.query_named("nice pose", p2)

        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


        
