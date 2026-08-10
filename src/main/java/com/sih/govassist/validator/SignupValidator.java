package com.sih.govassist.validator;

import com.sih.govassist.dto.request.SignupRequest;

public interface SignupValidator {


    ValidationResult validate(SignupRequest request);
}


