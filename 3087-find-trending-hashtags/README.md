<h2><a href="https://leetcode.com/problems/find-trending-hashtags/">3087. Find Trending Hashtags</a></h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Tweets</code></p>

<pre>+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| tweet_id    | int     |
| tweet_date  | date    |
| tweet       | varchar |
+-------------+---------+
tweet_id is the primary key (column with unique values) for this table.
Each row of this table contains user_id, tweet_id, tweet_date and tweet.
</pre>

<p>Write a solution to find the <strong>top</strong> <code>3</code> trending <strong>hashtags</strong>&nbsp;in&nbsp;<strong>February</strong> <code>2024</code>. Each tweet only contains one hashtag.</p>

<p>Return <em>the result table orderd by count of hashtag, hashtag in </em><strong>descending</strong><em> order.</em></p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p>Tweets table:</p>

<pre class="example-io">+---------+----------+----------------------------------------------+------------+
| user_id | tweet_id | tweet                                        | tweet_date |
+---------+----------+----------------------------------------------+------------+
| 135     | 13       | Enjoying a great start to the day! #HappyDay | 2024-02-01 |
| 136     | 14       | Another #HappyDay with good vibes!           | 2024-02-03 |
| 137     | 15       | Productivity peaks! #WorkLife                | 2024-02-04 |
| 138     | 16       | Exploring new tech frontiers. #TechLife      | 2024-02-04 |
| 139     | 17       | Gratitude for today's moments. #HappyDay     | 2024-02-05 |
| 140     | 18       | Innovation drives us. #TechLife              | 2024-02-07 |
| 141     | 19       | Connecting with nature's serenity. #Nature   | 2024-02-09 |
+---------+----------+----------------------------------------------+------------+
 </pre>

<p><strong>Output:</strong></p>

<pre class="example-io">+-----------+--------------+
| hashtag   | hashtag_count|
+-----------+--------------+
| #HappyDay | 3            |
| #TechLife | 2            |
| #WorkLife | 1            |
+-----------+--------------+

</pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li><strong>#HappyDay:</strong> Appeared in tweet IDs 13, 14, and 17, with a total count of 3 mentions.</li>
	<li><strong>#TechLife:</strong> Appeared in tweet IDs 16 and 18, with a total count of 2 mentions.</li>
	<li><strong>#WorkLife:</strong> Appeared in tweet ID 15, with a total count of 1 mention.</li>
</ul>

<p><b>Note:</b> Output table is sorted in descending order by hashtag_count and hashtag respectively.</p>
</div>
</div>