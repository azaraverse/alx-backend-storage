-- A SQL script that creates a stored procedure ComputeAverageScoreForUser() that computes and stores the average score for a student.

DELIMITER $$
-- Drop stored procedure if exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
-- Create stored procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Update the users table with the computed weighted average score
    UPDATE users
    SET average_score = (
        SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
        FROM corrections, projects
        WHERE corrections.user_id = user_id
        AND corrections.project_id = projects.id
    )
    WHERE id = user_id;
END $$
DELIMITER ;
