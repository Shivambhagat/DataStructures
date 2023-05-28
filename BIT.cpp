class BIT {
private:
    int n;
    vector<int> a;

public:
    BIT(int n) : n(n + 1), a(n + 1, 0) {}

    void update(int i, int val) {
        while (i < n) {
            a[i] += val;
            i += (i & (-i));
        }
    }

    int sum(int i) {
        int s = 0;
        while (i > 0) {
            s += a[i];
            i -= (i & (-i));
        }
        return s;
    }
};
