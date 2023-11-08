bool isReachableAtTime(int sx, int sy, int fx, int fy, int t){
    // special case
    if ((sx == fx) && (sy == fy)) {
        return t != 1;
    }
    int xdiff = fx - sx;
    int ydiff = fy - sy;
    if (xdiff < 0)
    xdiff = - xdiff;
    if (ydiff <0)
    ydiff = - ydiff;
    int max = (xdiff > ydiff)? xdiff : ydiff;
    return max <= t;
}