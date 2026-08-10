package com.sih.govassist.validator.impl;

import com.sih.govassist.dto.request.SignupRequest;
import com.sih.govassist.repository.UserRepository;
import com.sih.govassist.validator.SignupValidator;
import com.sih.govassist.validator.ValidationResult;
import org.springframework.stereotype.Component;

@Component
public class SignupValidatorImpl implements SignupValidator {
    private final UserRepository userRepository;

    public SignupValidatorImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public ValidationResult validate(SignupRequest request) {
        if (request.getName() == null ||
                request.getName().trim().isEmpty()) {

            return new ValidationResult(
                    false,
                    "Name cannot be empty"
            );
        }

        // Validate email
        if (request.getEmail() == null ||
                request.getEmail().trim().isEmpty()) {

            return new ValidationResult(
                    false,
                    "Email cannot be empty"
            );
        }

        // Check whether email already exists
        if (userRepository.existsByEmail(request.getEmail())) {

            return new ValidationResult(
                    false,
                    "Email already exists"
            );
        }

        return new ValidationResult(
                true,
                "Validation successful"
        );
    }
}
