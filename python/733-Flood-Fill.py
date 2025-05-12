class Solution:
    # Space O(n*m)
    # Time O(n*m)
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # Avoid infinite loop if starting and goal colors are same
        if image[sr][sc] == color:
            return image
        # Run fill helper function starting at given position
        self.fill(image, sr, sc, color, image[sr][sc])

        return image

    def fill(self, image, sr, sc, color, oldColor):
        # Exit without doing anything if the row or col value is out of bounds
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        # If the current position is not the same color as the color getting replaced, exit
        if image[sr][sc] != oldColor:
            return
        # Replace the current position value since it's in bounds and is the right color
        image[sr][sc] = color
        # Run the fill function in all 4 directions
        self.fill(image, sr - 1, sc, color, oldColor)
        self.fill(image, sr + 1, sc, color, oldColor)
        self.fill(image, sr, sc - 1, color, oldColor)
        self.fill(image, sr, sc + 1, color, oldColor)
