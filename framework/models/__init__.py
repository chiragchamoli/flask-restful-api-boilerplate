# Author: Chirag Chamoli
# -*- coding: utf-8 -*-
from aahho.ext.pymongo import AMongo

conn = AMongo()
db = conn.client_inst()

from aahho.models.users import UserModel
from aahho.models.blog import BlogsModel
from aahho.models.blog_posts import BlogsPostsModel
from aahho.models.sites import SitesModel
from aahho.models.users_sites import UsersSitesModel