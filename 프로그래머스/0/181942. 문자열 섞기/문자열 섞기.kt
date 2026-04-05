class Solution {
    fun solution(str1: String, str2: String): String {
        return buildString {
            for (i in str1.indices) {
                append("${str1[i]}${str2[i]}")
            }
        }
    }
}