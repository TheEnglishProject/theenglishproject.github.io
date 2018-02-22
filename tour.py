import facebook
import json
import sys
import os
import datetime
import dateutil.parser as dp

def get_skeleton_html():
    with open("skel_head.html", 'r') as skel:
        skel_head = skel.read()
    skel.close()
    with open("skel_foot.html", 'r') as skel:
        skel_foot = skel.read()
    skel.close()
    skeleton = {"head": skel_head, "foot": skel_foot}
    return skeleton
        
def gen_body_html(events_list):
    td_html = """
            <tr>
                <td> {} </td>
                <td> {} </td>
                <td> {} </td>
                <td><a target="_blank" href="https://www.facebook.com/events/{}">{}</a></td>
            </tr>
    """
    header = """
    <div class="container">
        <table class="table table-hover table-responsive">
            <caption><h3>Upcoming Shows</h3></caption>
            <tr>
                <th> Date </th>
                <th> Venue </th>
                <th> City </th>
                <th> Facebook Event </th>
            </tr>
    """
    footer = """
        </table>
    </div>
    """
    body = ""
    tag_place = "place"
    tag_location = "location"
    NONE_SPECIFIED = "None Specified"
    for event in reversed(events_list):
        ev_start = event["start_time"]
        ev_start_dt = dp.parse(ev_start)
        ev_date = "{} {}".format(ev_start_dt.strftime("%B"), ev_start_dt.day)
        ev_venue = NONE_SPECIFIED
        ev_city = NONE_SPECIFIED
        ev_state = NONE_SPECIFIED
        ev_place = NONE_SPECIFIED
        if tag_place in event:
            ev_venue = event["place"]["name"]
            if tag_location in event[tag_place]:
                ev_city = event["place"]["location"]["city"]
                ev_state = event["place"]["location"]["state"]
                ev_place = "{}, {}".format(ev_city, ev_state)
        ev_name = event["name"]
        ev_id = event["id"]
        body += td_html.format(ev_date,ev_venue,ev_place,ev_id,ev_name)

    body_html = header + body + footer
    return body_html
def get_facebook_graph():
    f = open('access_token.txt', 'r')
    access_token = f.read()
    f.close()
    graph = facebook.GraphAPI(access_token=access_token)
    return graph

if __name__ == "__main__":
    html_filename = "tour.html"
    fb_req = "TheEnglishProjectFunk/events?include_cancelled=false&time_filter=upcoming"
    graph = get_facebook_graph()
    events = graph.get_object(fb_req)
    body_html = gen_body_html(events["data"])
    skeleton = get_skeleton_html()
    full_html = skeleton["head"] + body_html + skeleton["foot"]

    with open(html_filename, 'w') as tour:
       tour.write(full_html)
    tour.close()
