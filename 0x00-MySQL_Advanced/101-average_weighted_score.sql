-- A SQL script that creates a stored procedure ComputeAverageScoreForUser() that computes and stores the average score for a student.

DELIMITER $$
-- Drop stored procedure if exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers $$
-- Create stored procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- declare variables
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 1;
    DECLARE average_weighted_score FLOAT DEFAULT 0;

    -- calculate the total weighted score and total weight for the given user
    SELECT SUM(corrections.score * projects.weight), SUM(projects.weight)
    INTO total_weighted_score, total_weight
    FROM corrections, projects
    WHERE corrections.project_id = projects.id
    AND corrections.user_id = users.id;

    -- calculate the average weighted score
    SET average_weighted_score = total_weighted_score / total_weight;

    -- Update the users table with the computed weighted average score
    UPDATE users
    SET average_score = average_weighted_score
    WHERE id = users.id;
END $$
DELIMITER ;
