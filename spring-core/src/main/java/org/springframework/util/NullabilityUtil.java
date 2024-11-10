package org.springframework.util;

import org.springframework.lang.Nullable;

public class NullabilityUtil {

	public static <T> T castToNonNullType(@Nullable T obj) {
		if(obj == null) {
			throw new IllegalArgumentException("Object must not be null");
		}
		return obj;
	}
}
