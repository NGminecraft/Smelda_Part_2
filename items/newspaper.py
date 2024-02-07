import webbrowser
import sys

class Newspaper():
    def test():
        loc = sys.path[0]
        loc = loc.split("//")
        del loc[-1]
        loc.append("Legend_of_Zink_Asset_Pack\Legend_of_Zink_Asset_Pack\Collectables\WebBest.html")
        loc = "//".join(loc)
        print(loc)

        webbrowser.open_new_tab()
        
    def get_ids():
        return {"consumable": False}