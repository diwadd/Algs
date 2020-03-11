#include <bits/stdc++.h> 

using namespace std;

class EndPoint {
    public:
        EndPoint(int px, int py, int plr, int pid): x(px), y(py), lr(plr), id(pid) {}
        EndPoint() {x = 0; y = 0; lr = 0; id = 0;}
        int x;
        int y;
        int lr;
        int id;
        friend bool operator< (const EndPoint &ep1, const EndPoint &ep2);
};

class Segment {
    public:
        Segment(EndPoint sp1, EndPoint sp2, int sid): p1(sp1), p2(sp2), id(sid) {}
        Segment() {p1 = EndPoint(); p2 = EndPoint(); id = 0;}
        EndPoint p1;
        EndPoint p2;
        int id;

        friend bool operator< (const Segment &s1, const Segment &s2);

    // void operator=(const Segment &s) { 
    //     p1 = s.p1;
    //     p2 = s.p2;
    //     id = s.id;
    // }
};

bool operator< (const Segment &s1, const Segment &s2){

    EndPoint ep1 = s1.p1;
    EndPoint ep1 = s1.p1;

    if (ep1.x > ep2.x) {
        return false;
    }

    if (ep1.x < ep2.x) {
        return true;
    }

    if (ep1.y >= ep2.y) {
        return false;
    }

    if (ep1.y < ep2.y) {
        return true;
    }

    if (ep1.lr > ep2.lr) {
        return false;
    }

    if (ep1.lr < ep2.lr) {
        return true;
    }
}


bool operator< (const EndPoint &ep1, const EndPoint &ep2){

    return ep1.y > ep2.y;
}

// bool operator< (const Segment &s1, const Segment &s2){

//     return ep1.y > ep2.y;
// }

ostream& operator<<(ostream& os, const EndPoint& ep)
{
    os << ep.x << " " << ep.y << " " << ep.lr;
    return os;
}

bool end_point_compare(const EndPoint &ep1, const EndPoint &ep2)
{

    if (ep1.x > ep2.x) {
        return false;
    }

    if (ep1.x < ep2.x) {
        return true;
    }

    if (ep1.y >= ep2.y) {
        return false;
    }

    if (ep1.y < ep2.y) {
        return true;
    }

    if (ep1.lr > ep2.lr) {
        return false;
    }

    if (ep1.lr < ep2.lr) {
        return true;
    }

}


int main() {

    vector<EndPoint> end_points;
    map<int, Segment> segments;
    
    vector<int> vxs = { 1, 2,  2, 3,  3, 4,  4, 5,  5, 6,  2, 6};
    vector<int> vys = { 1, 2,  2, 4,  4, 5,  5, 7,  7, 2,  6, 6};
    vector<int> vlr = {-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1};
    vector<int> vid = { 1, 1,  2, 2,  3, 3,  4, 4,  5, 5,  6, 6};

    for(int i = 1; i < vxs.size(); i = i + 2) {
        int x2 = vxs[i];
        int y2 = vys[i];
        int lr2 = vlr[i];
        int id2 = vid[i];

        int x1 = vxs[i-1];
        int y1 = vys[i-1];
        int lr1 = vlr[i-1];
        int id1 = vid[i-1];

        EndPoint p2 = EndPoint(x2, y2, lr2, id2);
        EndPoint p1 = EndPoint(x1, y1, lr1, id1);

        segments[id1] = Segment(p1, p2, id1);
        end_points.push_back(p1);
        end_points.push_back(p2);
    }



    cout << "Before sort" << endl;
    for(auto ep : end_points){
        cout << ep << endl;
    }

    sort(end_points.begin(), end_points.end(), end_point_compare);

    cout << "After sort" << endl;
    for(auto ep : end_points){
        cout << ep << endl;
    }

    // map<int, int> status;
    set<Segment> status;
    for(int i = 0; i < end_points.size(); i++){ 
        if (end_points[i].lr == -1){
            int id = end_points[i].id;
            status.insert(segments[id]);

            set<EndPoint>::iterator uitr = status.upper_bound();

            if(uitr != status.end()){

                
                if(){

                }

            }



        }


    }

}