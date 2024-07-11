-- A SQL script that creates a stored procedure ComputeAverageScoreForUser() that computes and stores the average score for a student.

DELIMITER $$
-- Drop stored procedure if exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers $$
-- Create stored procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Update the users table with the computed weighted average score for each user
    -- by joining it with a derived table calculating the weighted score
    UPDATE users
    JOIN(
        SELECT
            corrections.user_id,
            SUM(corrections.score * projects.weight) / SUM(projects.weight) AS average_weighted_score
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        GROUP BY corrections.user_id
    ) AS derived
    ON users.id = derived.user_id

    SET users.average_score = derived.average_weighted_score;
END $$
DELIMITER ;
