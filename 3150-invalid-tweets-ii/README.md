<h2><a href="https://leetcode.com/problems/invalid-tweets-ii/">3150. Invalid Tweets II</a></h2><h3>Easy</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Tweets</code></p>

<pre>+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.
</pre>

<p>Write a solution to find <strong>invalid tweets</strong>. A tweet is considered invalid if it meets <strong>any</strong> of the following criteria:</p>

<ul>
	<li>It exceeds <code>140</code> characters in length.</li>
	<li>It has more than <code>3</code> mentions.</li>
	<li>It includes more than <code><font face="monospace">3</font></code>&nbsp;hashtags.</li>
</ul>

<p>Return <em>the result table ordered by</em> <code>tweet_id</code> <em>in <strong>ascending</strong> order</em>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong>Example:</strong></p>

<div class="example-block">
<p><strong>Input:</strong></p>

<p>Tweets table:</p>

<pre class="example-io">  +----------+-----------------------------------------------------------------------------------+
  | tweet_id | content                                                                           |
  +----------+-----------------------------------------------------------------------------------+
  | 1        | Traveling, exploring, and living my best life @JaneSmith @SaraJohnson @LisaTaylor |
  |          | @MikeBrown #Foodie #Fitness #Learning                                             | 
  | 2        | Just had the best dinner with friends! #Foodie #Friends #Fun                      |
  | 4        | Working hard on my new project #Work #Goals #Productivity #Fun                    |
  +----------+-----------------------------------------------------------------------------------+
  </pre>

<p><strong>Output:</strong></p>

<pre class="example-io">  +----------+
  | tweet_id |
  +----------+
  | 1        |
  | 4        |
  +----------+
  </pre>

<p><strong>Explanation:</strong></p>

<ul>
	<li>tweet_id&nbsp;1 contains 4&nbsp;mentions.</li>
	<li>tweet_id 4 contains 4 hashtags.</li>
</ul>
Output table is ordered by tweet_id in ascending order.</div>
</div>