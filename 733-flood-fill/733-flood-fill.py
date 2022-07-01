class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions=[[0,-1],[0,1],[1,0],[-1,0]]
        target=image[sr][sc]
        if target==color:
            return image
        def helper(image,row,col):
            image[row][col]=color
            
            for x,y in directions:
                if 0<=row+x<len(image) and \
                0<=col+y<len(image[0]) and \
                image[row+x][col+y]==target:
                    image=helper(image,row+x,col+y)
            return image
        return helper(image,sr,sc)
        