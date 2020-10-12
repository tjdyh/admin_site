from flask import render_template
from . import nssite

# site_name = "倚天系统"
# yt = 'http://scm.51eanj.com'
ns_list = [{'ns_name': '倚天系统','ns_addr': 'http://scm.51eanj.com'},{'ns_name': '蚁掌柜系统','ns_addr': 'http://eboss.51eanj.com'}]

@nssite.route('/nslist')
def nslist():
    return render_template('nssite/nslist.html',ns_list=ns_list)
