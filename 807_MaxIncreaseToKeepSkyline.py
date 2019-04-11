class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #the transpose of grid
        grid_t_it= zip(*grid);
        grid_t = list(grid_t_it);

        #let the dimension of grid = (m,n)
        m=len(grid);
        n=len(grid_t);

        #find the horizontal/vertical skyline hsl/vsl viewd from h/v
        #hsl is visually a row vector, vsl a column
        vsl = list(map(max,grid));#vsl is visually a column
        hsl = list(map(max,grid_t));#hsl is visually a row

        #return sum, sum(grid_new - grid)
        #grid_new[i][j] = min(hsl[i], vsl[j])
        sum=0;
        for i in range(m):
            for j in range(n):
                sum += min(hsl[i],vsl[j]) - grid[i][j];
        return sum
